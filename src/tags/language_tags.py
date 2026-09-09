from django import template

register = template.Library()

_LANG_TO_COUNTRY = {
    "af": "ZA",       # Afrikaans
    "ar": "EG",       # Arabic
    "ar-dz": "DZ",    # Algerian Arabic
    "ast": "ES",      # Asturian
    "az": "AZ",       # Azerbaijani
    "bg": "BG",       # Bulgarian
    "be": "BY",       # Belarusian
    "bn": "BD",       # Bengali
    "br": "FR",       # Breton
    "bs": "BA",       # Bosnian
    "ca": "ES",       # Catalan
    "ckb": "IQ",      # Central Kurdish (Sorani)
    "cs": "CZ",       # Czech
    "cy": "GB",       # Welsh
    "da": "DK",       # Danish
    "de": "DE",       # German
    "dsb": "DE",      # Lower Sorbian
    "el": "GR",       # Greek
    "en": "GB",       # English
    "en-au": "AU",    # Australian English
    "en-gb": "GB",    # British English
    "eo": "",         # Esperanto (no country)
    "es": "ES",       # Spanish
    "es-ar": "AR",    # Argentinian Spanish
    "es-co": "CO",    # Colombian Spanish
    "es-mx": "MX",    # Mexican Spanish
    "es-ni": "NI",    # Nicaraguan Spanish
    "es-ve": "VE",    # Venezuelan Spanish
    "et": "EE",       # Estonian
    "eu": "ES",       # Basque
    "fa": "IR",       # Persian
    "fi": "FI",       # Finnish
    "fr": "FR",       # French
    "fy": "NL",       # Frisian
    "ga": "IE",       # Irish
    "gd": "GB",       # Scottish Gaelic
    "gl": "ES",       # Galician
    "he": "IL",       # Hebrew
    "hi": "IN",       # Hindi
    "hr": "HR",       # Croatian
    "hsb": "DE",      # Upper Sorbian
    "ht": "HT",       # Haitian Creole
    "hu": "HU",       # Hungarian
    "hy": "AM",       # Armenian
    "ia": "",         # Interlingua (no country)
    "id": "ID",       # Indonesian
    "ig": "NG",       # Igbo
    "io": "",         # Ido (no country)
    "is": "IS",       # Icelandic
    "it": "IT",       # Italian
    "ja": "JP",       # Japanese
    "ka": "GE",       # Georgian
    "kab": "DZ",      # Kabyle
    "kk": "KZ",       # Kazakh
    "km": "KH",       # Khmer
    "kn": "IN",       # Kannada
    "ko": "KR",       # Korean
    "ky": "KG",       # Kyrgyz
    "lb": "LU",       # Luxembourgish
    "lt": "LT",       # Lithuanian
    "lv": "LV",       # Latvian
    "mk": "MK",       # Macedonian
    "ml": "IN",       # Malayalam
    "mn": "MN",       # Mongolian
    "mr": "IN",       # Marathi
    "ms": "MY",       # Malay
    "my": "MM",       # Burmese
    "nb": "NO",       # Norwegian Bokmål
    "ne": "NP",       # Nepali
    "nl": "NL",       # Dutch
    "nn": "NO",       # Norwegian Nynorsk
    "os": "GE",       # Ossetic
    "pa": "PK",       # Punjabi
    "pl": "PL",       # Polish
    "pt": "PT",       # Portuguese
    "pt-br": "BR",    # Brazilian Portuguese
    "ro": "RO",       # Romanian
    "ru": "RU",       # Russian
    "sk": "SK",       # Slovak
    "sl": "SI",       # Slovenian
    "sq": "AL",       # Albanian
    "sr": "RS",       # Serbian
    "sr-latn": "RS",  # Serbian Latin
    "sv": "SE",       # Swedish
    "sw": "KE",       # Swahili
    "ta": "IN",       # Tamil
    "te": "IN",       # Telugu
    "tg": "TJ",       # Tajik
    "th": "TH",       # Thai
    "tk": "TM",       # Turkmen
    "tr": "TR",       # Turkish
    "tt": "RU",       # Tatar
    "udm": "RU",      # Udmurt
    "ug": "CN",       # Uyghur
    "uk": "UA",       # Ukrainian
    "ur": "PK",       # Urdu
    "uz": "UZ",       # Uzbek
    "vi": "VN",       # Vietnamese
    "zh-hans": "CN",  # Simplified Chinese
    "zh-hant": "TW",  # Traditional Chinese
}

@register.filter
def lang_flag(lang_code):
    if not lang_code:
        return ""
    country = _LANG_TO_COUNTRY.get(str(lang_code).lower())
    if not country:
        return ""
    return f"fi fi-{country.lower()}"


@register.filter
def flag(country_code):
    if not country_code:
        return ""
    return f"fi fi-{country_code.lower()}"
