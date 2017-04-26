# Changelog

> All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/springload/wagtaildraftail/compare/v0.5.0...HEAD)

...

## [[v0.5.0]](https://github.com/springload/draftjs_exporter/releases/tag/v0.5.0)

### Add

- Hooks to register custom components.

### Changed

- Update to latest version of `draftjs_exporter`.

### Fixed

- LinkDecorator now correctly output links for internal pages.


## [[v0.4.1]](https://github.com/springload/draftjs_exporter/releases/tag/v0.4.1)

### Fixed

- Fixed error for block/field with default value.

## [[v0.4.0]](https://github.com/springload/draftjs_exporter/releases/tag/v0.4.0)

### Add

- Equality check for DraftText nodes.
- Add default entity strategy.

### Changed

- Rename the default editor to `default_draftail`.
- Rename the `utilities` module to `utils` to follow Django convention.
- Rename `JsonTextArea` widget to `DraftailTextArea`.
- Move the `get_exporter_config` from the `settings` module to the `utils` module.
- Move entity `decorator` and `source` definition to Python.
- Bumped `draftjs_exporter` dependency to `0.8.0`. See the updated example configuration below or the module's [changelog](https://github.com/springload/draftjs_exporter/blob/v0.8.0/CHANGELOG.md#v080) for a full list of changes.


## [[v0.3.0]](https://github.com/springload/draftjs_exporter/releases/tag/v0.3.0)

### Added

- DraftText(RichText) implementation
- New DraftailTextBlock using new DraftText implementation
- Support for Python 3.6

### Removed

- Remove custom filters
- Remove custom template tags

### Fixed

- Fix blocks.py import paths
- Fix DraftailTextField prep_value generation for Django>1.8

## [[v0.2.2]](https://github.com/springload/draftjs_exporter/releases/tag/v0.2.2)

### Fixed

- Add missing `get_document_meta` utility function – up until now documents rendered a (todo todo) placeholder instead of their metadata. #21

## [[v0.2.1]](https://github.com/springload/draftjs_exporter/releases/tag/v0.2.1)

### Fixed

- Fix documentation formatting.

## [[v0.2.0]](https://github.com/springload/draftjs_exporter/releases/tag/v0.2.0)

### Added

- Tests! Linting! Quality control!

### Changed

- Rename `Source` components.

### Fixed

- Fix incorrect documentation.
- Fix imports not working.
- Fix Python compat issue.

## [[v0.1.0]](https://github.com/springload/draftjs_exporter/releases/tag/v0.1.0)

First usable release!

-------------

## [[x.y.z]](https://github.com/springload/draftjs_exporter/releases/tag/x.y.z) (Template: http://keepachangelog.com/)

### Added

- Something was added to the API / a new feature was introduced.

### Changed

### Fixed

### Removed
