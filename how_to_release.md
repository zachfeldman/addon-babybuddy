0. Make your new code branch
1. Ensure you bump the version in `babybuddy/config.yaml`
2. Create a tag, point at the new branch from step 0. and number the tag the same as in step 1.
3. Wait for the build to create and publish the tag to GHCR
4. Merge code into main branch, this will allow all Home Assistant installs to know a new version is available.

