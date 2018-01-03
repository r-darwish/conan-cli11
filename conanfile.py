#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class LibnameConan(ConanFile):
    name = "cli11"
    version = "1.3.0"
    description = "Command line parser for C++11"
    url = "https://github.com/bincrafters/conan-cli11"
    license = "BSD 3-Clause"
    exports = ["LICENSE.md"]

    def source(self):
        source_url = "https://github.com/CLIUtils/CLI11"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "CLI11-" + self.version
        os.rename(extracted_dir, "sources")

    def package(self):
        self.copy(pattern="LICENSE", src="sources")
        self.copy(pattern="*", dst="include", src="sources/include")

    def package_id(self):
        self.info.header_only()
