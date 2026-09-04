#!/usr/bin/env bash

set -e
set -o pipefail
set -v

# Stackbit project was deleted upstream (their API returns "Project not found"),
# which broke every Netlify deploy. Build the Gatsby site directly instead.
gatsby build
