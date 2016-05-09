# LK

The LK embedded kernel. An SMP-aware kernel designed for small systems.

See https://github.com/littlekernel/lk for the latest version.

See https://github.com/littlekernel/lk/wiki for documentation.

## to build with GN for x64 and ARM64 on linux

0. run `sudo apt-get install ninja-build` to install Ninja

1. build toolchains for aarch64 and x86_64:

   ```bash
   cd $SRC
   git clone https://github.com/travisg/toolchains.git
   cd toolchains
   ./doit -a 'arm i686 aarch64 x86_64' -f -j32
   export PATH=$SRC/toolchains/aarch64-elf-5.3.0-Linux-x86_64/bin:$SRC/toolchains/x86_64-elf-5.3.0-Linux-x86_64/bin:$PATH
   ```

2. build and install qemu:

   ```bash
   cd $SRC
   git clone http://git.qemu.org/git/qemu.git
   cd qemu
   ./configure --target-list=aarch64-softmmu,x86_64-softmmu
   make -j32
   ```

3. run `scripts/download-gn.sh` (from the lk directory) to download GN

4. run GN to generate Ninja build script:

   ```bash
   ./gn gen out/x64 --args='target_cpu = "x64"'
   ./gn gen out/arm64 --args='target_cpu = "arm64"'
   ```

5. run Ninja to build the lk:

  ```bash
  ninja -C out/x64
  ninja -C out/arm64
  ```

6. run lk using qemu:

  ```bash
  qemu/x86_64-softmmu/qemu-system-x86_64 -m 512 -kernel out/x64/kernel.bin -nographic
  qemu/aarch64-softmmu/qemu-system-aarch64 -machine virt -cpu cortex-a53 -m 512 -kernel out/arm64/kernel.elf -nographic
  ```

This will get you a interactive prompt into LK which is running in qemu
arm machine 'virt' emulation. type 'help' for commands.
