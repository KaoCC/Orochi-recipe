
from conans import ConanFile, tools

required_conan_version = ">=1.43.0"

class OrochiConan(ConanFile):
    name = "orochi"
    homepage = "https://github.com/GPUOpen-LibrariesAndSDKs/Orochi"

    description = "Orochi is a library loading HIP and CUDA APIs dynamically, allowing the user to switch APIs at runtime."
    license = "MIT"

    no_copy_source = True

    version = "latest"

    @property
    def _source_subfolder(self):
        return "source_subfolder"


    def source(self):
        # tools.get(**self.conan_data["sources"][self.version], destination=self._source_subfolder, strip_root=True)

        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://github.com/GPUOpen-LibrariesAndSDKs/Orochi.git", "main")


    def package(self):
        self.copy(pattern="LICENSE*", src = self._source_subfolder, dst="licenses")
        self.copy("Orochi/*.h", src = self._source_subfolder, dst="include")
        self.copy("Orochi/*.cpp", src = self._source_subfolder, dst="include")
        self.copy("contrib/cuew/*", src = self._source_subfolder, dst="include")
        self.copy("contrib/hipew/*", src = self._source_subfolder, dst="include")


    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "orochi"
        self.cpp_info.names["cmake_find_package_multi"] = "orochi"
        self.cpp_info.names["pkg_config"] = "orochi"