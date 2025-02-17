# FOnline Engine

## Tools

1. [Git](https://git-scm.com/downloads)
2. [CMake](https://cmake.org/download/)
3. [Chocolatey](https://chocolatey.org/)
4. [Visual Studio 2017 Community](https://visualstudio.microsoft.com/vs/older-downloads/)
5. [Visual Studio Express 2010](https://learn.microsoft.com/en-us/lifecycle/products/visual-studio-2010)
6. [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net481)
7. (Optional) Windows SDK for Windows 7 which has compiler tools v100 (Visual Studio Express 2010 has these tools too)

## Setup environment

1. Install Git.
2. Install CMake.
3. Install Chocolatey (run Windows PowerShell as administrator).

    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

4. Install Visual Studio 2017 (use Chocolatey).

    ```powershell
    choco install visualstudio2017community
    ```

5. Install .NET Framework 4.8.
6. Install Visual Studio Express 2010 (compiler tools v100):
   1. Create [Microsoft account](https://account.microsoft.com/account/manage-my-account).
   2. Join [Visual Studio Dev Essentials](https://visualstudio.microsoft.com/dev-essentials/).
   3. Open [Visual Studio Subscriptions](https://my.visualstudio.com/Downloads?q=visual%20studio%202010).
   4. Download `en_visual_studio_2010_express_x86_dvd_510419.iso`.

## Build engine

1. Open `FOnline-BraveNewWorld/foclassic/SDK_V7`.
2. Run:

    ```text
    cmake -G "Visual Studio 15" -T v100 ../
    ```

3. Open `FOnline-BraveNewWorld/foclassic/SDK_V7/FOClassic.sln`.
4. Build solution by using `Build/Build Solution`.
5. Open `FOnline-BraveNewWorld/foclassic/SDK_V7/FOClassic-v7`.
6. Copy `*.exe` and `*.pdb` files to directories in `FOnline-BraveNewWorld\PReloaded`.

## Resources

1. [FOClassic tutorials/Setting up FOClassic](https://fodev.net/forum/index.php/topic,30344.0.html)
2. [GitHub Sasabmeg](https://github.com/Sasabmeg)
