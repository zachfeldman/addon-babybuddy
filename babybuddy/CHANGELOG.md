# CHANGELOG

## 2.7.2
### 🚨 Breaking
- **armhf, armv7, and i386 builds are deprecated** and are no longer built in
  CI or release workflows.
  Home Assistant Community Add-ons dropped those architectures in base image
  [v19.0.0](https://github.com/hassio-addons/app-base/releases/tag/v19.0.0).
  The addon base image is now aligned with supported platforms (e.g. aarch64,
  amd64); users on dropped hardware need an older addon release or a
  supported board.
### ⬆️ Updated
- Addon version bump; still bundles Baby Buddy
  [2.7.1](https://github.com/babybuddy/babybuddy/releases/tag/v2.7.1).
- Bumped hassio addon base image to
  [20.0.1](https://github.com/hassio-addons/app-base/releases/tag/v20.0.1)
  so container builds resolve current Alpine/OpenSSL packages and CI tests
  can run.
- CI “Build Addon” workflow now only builds **aarch64** and **amd64** (see
  breaking note above).
- `babybuddy/config.yaml` lists only **aarch64** and **amd64** under `arch`
  (see breaking note).
- `babybuddy/build.yaml` `build_from` lists only **aarch64** and **amd64**
  (see breaking note).
- `publish-container` workflow publishes only **aarch64** and **amd64** (see
  breaking note).

## 2.7.1
### ⬆️ Updated
- Updated to Baby Buddy [2.7.1](https://github.com/babybuddy/babybuddy/releases/tag/v2.7.1)
### 🐞 Fixed
- [Custom child images](https://github.com/OttPeterR/addon-babybuddy/pull/84)

## 2.7.0
### ⬆️ Updated
- Updated to Baby Buddy [2.7.0](https://github.com/babybuddy/babybuddy/releases/tag/v2.7.0)

## 2.6.3
### ⬆️ Updated
- Updated to Baby Buddy [2.6.3](https://github.com/babybuddy/babybuddy/releases/tag/v2.6.3)

## 2.6.2
### ⬆️ Updated
- Updated to Baby Buddy [2.6.2](https://github.com/babybuddy/babybuddy/releases/tag/v2.6.2)
- Updated add on base to [16.3.4](https://github.com/hassio-addons/addon-base/releases/tag/v16.3.4)

## 2.2.1.1
### ⬆️ Updated
- Fix for notifications that keep coming back

## 2.2.1

### ⬆️ Updated
- Baby Buddy to 2.2.1 [release notes](https://github.com/babybuddy/babybuddy/releases/tag/v2.2.1)
- HA HAddon base to 15.0.6

## 2.2.0

### 🆕 Added
- this nifty changelog

### ⬆️ Updated
- Baby Buddy to 2.2.0 [release notes](https://github.com/babybuddy/babybuddy/releases/tag/v2.2.0)
- HA Addon base to 15.0.5 [release notes](https://github.com/hassio-addons/addon-base/releases/tag/v15.0.5)
