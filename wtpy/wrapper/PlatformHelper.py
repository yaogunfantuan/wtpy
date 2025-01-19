import platform

class PlatformHelper:

    @staticmethod
    def isPythonX64() -> bool:
        ret = platform.architecture()
        return (ret[0] == "64bit")

    @staticmethod
    def isWindows() -> bool:
        if "windows" in platform.system().lower():
            return True

        return False

    @staticmethod
    def isMacOS() -> bool:
        if "darwin" in platform.system().lower():
            return True
        return False

    @staticmethod
    def isMacOSArm() -> bool:
        if ("darwin" in platform.system().lower()
                and "arm" in platform.machine().lower()):
            return True
        return False

    @staticmethod
    def getModule(moduleName:str, subdir:str="") -> str:
        dllname = ""
        ext = ""
        prefix = ""
        if PlatformHelper.isWindows(): #windows平台
            ext = ".dll"
            if PlatformHelper.isPythonX64():
                dllname = "x64/"
            else:
                dllname = "x86/"
        elif PlatformHelper.isMacOS():
            if PlatformHelper.isMacOSArm():
                dllname = "macos_arm64/"
            else:
                dllname = "macos64/"
            prefix = "lib"
            ext = ".dylib"
        else:#Linux平台
            dllname = "linux/"
            prefix = "lib"
            ext = ".so"

        if subdir != "":
            dllname += subdir + "/"

        dllname += prefix + moduleName + ext
        return dllname
    
    @staticmethod
    def auto_encode(s:str) -> bytes:
        if PlatformHelper.isWindows():
            return bytes(s, encoding = "utf-8").decode('utf-8').encode('gbk')
        else:
            return bytes(s, encoding = "utf-8")
            