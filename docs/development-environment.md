Development Environments
========================

Setting up a development environment for the library is easy! We leverage a
few different tools on the host (e.g. Windows, Mac, or Linux), but aside from
those most of the requirements are sandboxed in a VM, so there is very little
work you need to do to get up and running.

#### Pre-requisites
 1. Install [Git](https://git-scm.com/)
 2. Install [VirtualBox](https://www.virtualbox.org/)
 3. Install [Vagrant](https://www.vagrantup.com/)

#### Setup Steps
In order to actually setup the development environment follow the steps below.

1. Clone the `dice-python` repository into your workspace, e.g.
   `~/workspace/dice-python`
2. Navigate to `dice-python` within your workspace, e.g.
   ```
   $ cd ~/workspace/dice-python
   ```
3. Open terminal to your workspace and start Vagrant, e.g.
   ```
   $ vagrant up
   ```
4. Once Vagrant has successfully completed its provisioning, enter the virtual
   machine using SSH _[1]_

---

## Notes

* **[1]** To use SSH on Windows you may use
  [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/); on Mac and
  Linux environments you may enter the Vagrant-managed virtual machine by
  issuing the command `vagrant ssh` from a terminal prompt within the
  `~/workspace/dice-python` directory.
