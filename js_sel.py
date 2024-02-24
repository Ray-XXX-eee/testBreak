# javascript_webdriverio_functions.py

import os


def create_js_webdriverio_project(project_directory):
    os.system(f"npm init -y")
    os.system(f"npm install webdriverio mocha chai --save-dev")

    os.makedirs(f"{project_directory}/test", exist_ok=True)

    with open(f"{project_directory}/wdio.conf.js", "w") as wdio_config_file:
        wdio_config_file.write(
            """
exports.config = {
    specs: [
        './test/**/*.js'
    ],
    capabilities: [{
        maxInstances: 5,
        browserName: 'chrome'
    }],
    logLevel: 'info',
    framework: 'mocha',
    mochaOpts: {
        ui: 'bdd',
        timeout: 60000
    },
    reporters: ['spec'],
}
"""
        )

    with open(f"{project_directory}/test/test_example.js", "w") as test_file:
        test_file.write(
            """
const assert = require('chai').assert;

describe('Example Test', () => {
    it('should have the correct title', () => {
        browser.url('https://example.com');
        const title = browser.getTitle();
        assert.strictEqual(title, 'Example Domain');
    });
});
"""
        )
