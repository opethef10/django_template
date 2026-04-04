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

## 0.8.0 - 2026-04-04

### Added

- django_htmx

## 0.7.0 - 2026-04-01

### Added

- Template documentation
- ReCAPTCHA support for signup form
- Generate script for Django secret key
- AGENTS.md

### Changed

- Default port for docker-compose.yml

## 0.6.4 - 2026-03-29

### Changed

- Remove subscriptions when a user is marked as inactive

## 0.6.3 - 2026-03-29

### Added

- Custom signup form with first name and last name fields

## 0.6.2 - 2026-03-29

### Added

- Translations

## 0.6.1 - 2026-03-29

### Changed

- Upgrade DataTables to v2.3.7

## 0.6.0 - 2026-03-28

### Changed

- Dockerfile and scripts

### Removed

- mobiledetect dependency

## 0.5.0 - 2026-03-27

### Added

- Accounts app
- Subscriptions app
- Dark mode
- Modal with fuzzy search
- compilemessages support for update script

### Changed

- Language selection menu in navbar
- User dropdown menu
- Allauth profile menus on the top

### Fixed

- Mobiledetect error in tests

## 0.4.4 - 2026-03-10

### Added

- Export DJANGO_SETTINGS_MODULE in update script

## 0.4.3 - 2026-03-06

### Changed

- Allauth settings

## 0.4.2 - 2026-03-06

### Security

- Upgrade libraries

## [0.4.1] - 2026-02-23

### Changed

- Navbar menu horizontal align
- Readjust accounts page layout

### Removed

- Allauth usersessions

## [0.4.0] - 2026-02-22

### Added

- Allauth honeypot field
- PWA install button
- Flatpage edit button for admins

### Changed

- Session cookie age to 1 year
- Don't send email to password reset users if email is not registered
- Locale to en_US

### Removed

- python-dotenv library
- LocaleMiddleware

## [0.3.1] - 2026-02-15

### Added

- Push script

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
