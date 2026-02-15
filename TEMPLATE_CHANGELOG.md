# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [major.minor.patch] - yyyy-mm-dd
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
-->

## [0.3.1] - 2026-02-15

### Changed

- Test script
- SelectRelatedModelAdmin to utils
- Dockerfile --no-cache-dir flag for pip
- Upgrade docker python to 3.13
- Library upgrades

### Removed

- urlresolvers
- Unused form tags

## [0.3.0] - 2025-10-17
### Added
- Social links in footer
### Changed
- ALLOWED_HOSTS to accept all hosts in development
- Template text to English

## [0.2.7] - 2025-09-18
### Changed
- Deprecated allauth fields

## [0.2.6] - 2025-09-17
### Fixed
- Database backup script bug

## [0.2.5] - 2025-06-20
### Changed
- docker-compose change restart policy

## [0.2.4] - 2025-06-18
### Changed
- Simplified PWA logo logic

## [0.2.3] - 2025-06-17
### Added
- .local urls to ALLOWED_HOSTS

## [0.2.2] - 2025-06-03
### Added
- PROJECT_PORT_NUMBER environment variable
### Changed
- Docker service name to `django_app`
### Removed
- site.webmanifest
### Security
- Upgrade libraries

## [0.2.1] - 2025-06-01
### Fixed
- .env.example file

## [0.2.0] - 2025-06-01
### Added
- EMAIL_ENABLED environment variable
- Optional signup
### Changed
- Recaptcha made optional
- Database file name
### Fixed
- Internalization of contact form
- PWA errors
- HTML meta tag urls
- HTML lang attribute made dynamic
- Allauth pages layout

## [0.1.0] - 2025-05-25
### Added
- Navbar and footer link menus
