# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/ubuntu-16.04"
  #config.vm.box_url = "https://atlas.hashicorp.com/bento/boxes/ubuntu-16.04"

  # SHARED FOLDERS:
  #
  # Create shared folders for Vagrant to interact with; the primary
  # development environment is rsync'd to the /vagrant folder, while
  # the VirtualBox share is created in the /shared directory, e.g.
  #
  #   /vagrant -> VirtualBox shared folder
  #
  config.vm.synced_folder ".", "/vagrant"

  ### VirtualBox Provider Configuration
  config.vm.provider :virtualbox do |vb|
    vb.gui = false
    vb.customize ["modifyvm", :id, "--cpus", "1"]
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/vagrant", "1"]
  end

  #: Prepare and boot the box.
  config.vm.provision :shell, path: "provision.sh"
end
