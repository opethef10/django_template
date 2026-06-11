from django.template import engines
from django.template.exceptions import TemplateDoesNotExist
from django.http import Http404


class MarkdownMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if URL ends with .md
        if request.path_info.endswith('.md'):
            # Store original path and mark as markdown
            request.original_path = request.path_info
            request.is_markdown = True
            # Strip .md for URL resolution
            request.path_info = request.path_info[:-3]
            if not request.path_info.endswith('/'):
                request.path_info += '/'
            request.path = request.path_info
        else:
            request.is_markdown = False
            request.original_path = request.path_info

        return self.get_response(request)

    def process_template_response(self, request, response):
        """Swap .html template to .md if markdown request"""
        if not getattr(request, 'is_markdown', False):
            return response

        if not hasattr(response, 'template_name'):
            return response

        template_name = response.template_name

        # Handle template lists (common with ListView/MultipleObjectTemplateResponseMixin)
        if isinstance(template_name, (list, tuple)):
            for t in template_name:
                md_template = self.get_md_template_name(t)
                if self.template_exists(md_template):
                    response.template_name = md_template
                    response['Content-Type'] = 'text/markdown; charset=utf-8'
                    return response
            raise Http404(f"Markdown template not found for: {template_name}")
        else:
            # Single template
            md_template = self.get_md_template_name(template_name)
            if self.template_exists(md_template):
                response.template_name = md_template
                response['Content-Type'] = 'text/markdown; charset=utf-8'
            else:
                raise Http404(f"Markdown template not found: {md_template}")

        return response

    def get_md_template_name(self, template_name):
        """Convert template name to .md version"""
        if template_name.endswith('.html'):
            return template_name.replace('.html', '.md')
        else:
            return template_name + '.md'

    def template_exists(self, template_name):
        """Check if template exists in any Django template engine"""
        for engine in engines.all():
            try:
                engine.get_template(template_name)
                return True
            except TemplateDoesNotExist:
                pass
        return False
