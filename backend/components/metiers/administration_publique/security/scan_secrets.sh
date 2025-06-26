#!/bin/bash

# Exit on any error
set -e

# Variables
MODULE_PATH="backend/components/metiers/administration_publique"
DEPENDENCY_SCAN_REPORT="dependency-scan-report.json"
SECRET_SCAN_REPORT="secret-scan-report.json"

echo "Security scan for the 'administration_publique' module"

# Step 1: Dependency Scan
echo "Running dependency scan..."
snyk test --json --file=$MODULE_PATH/package.json > $MODULE_PATH/$DEPENDENCY_SCAN_REPORT

# Step 2: Secret Scan
echo "Running secret scan..."
detect-secrets scan $MODULE_PATH > $MODULE_PATH/$SECRET_SCAN_REPORT

# Step 3: Check Reports
if [ -s $MODULE_PATH/$DEPENDENCY_SCAN_REPORT ] || [ -s $MODULE_PATH/$SECRET_SCAN_REPORT ]; then
    echo "Security issues detected. Please review the reports."
    exit 1
else
    echo "No security issues detected."
fi

echo "Security scan completed successfully."
