# Copyright (c) 2016 Sean Quinn
#
# It is illegal to use, reproduce or distribute any part of this
# Intellectual Property without prior written authorization from
# the designated copyright holder.vagrant.json.sample
require "json"

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

# The name of the file used for configuration overrides.
VAGRANTFILE_JSON_PROPERTIES_OVERRIDE = "vagrant.json"

# Assign the default provider to be
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

# Add "deep_merge" functionality to Hash
class ::Hash
    def deep_merge(second)
        merger = proc { |key, v1, v2| Hash === v1 && Hash === v2 ? v1.merge(v2, &merger) : [:undefined, nil, :nil].include?(v2) ? v1 : v2 }
        self.merge(second, &merger)
    end
end

#: Vagrantfile Configuration
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  #: Install the Ubuntu Vivid 64-bit server box...
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  #: The default properties that will be used for parts of the VM configuration,
  #: this should contain all of the sensible defaults to the values which are
  #: exposed to users for overriding. The ports are the ports that the guest VM
  #: will forward TO on the host (e.g. the host ports that will be opened).
  props = {
    "ip"                    => "dhcp",    # The default IP address.
    "ports" => {},                        #: The ports
    "share" => {                          #: The share type.
      "enabled"             => true,
      "type"                => "basic",
      "create"              => true,
      "mount_options"       => [],
    },
  }

  #: Test to see if the guest environment is being created on a Windows-based
  #: machine. If it is, we expect Cygwin to be installed (for access to rsync)
  #: and that cygwin is on the Windows path, e.g.
  #:
  #: CYGWIN_HOME = c:/cygwin64
  #: PATH = %PATH%;%CYGWIN_HOME%/bin
  #:
  #: For more information, see: https://github.com/mitchellh/vagrant/issues/4073
  begin
    @is_windows = (/cygwin|mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM) != nil
    if @is_windows
      msg =  "\n\n  NOTICE:\n"
      msg << "  Vagrant has detected that you are on a Windows-based platform.\n"
      msg << "  This environment requires cygwin for some of its operations, adding\n"
      msg << "  cygwin to detected OS.\n\n"
      msg << "  see: https://github.com/mitchellh/vagrant/issues/4073"
      msg << "\n\n\n"
      print msg

      ENV["VAGRANT_DETECTED_OS"] = ENV["VAGRANT_DETECTED_OS"].to_s + " cygwin"
    end
  rescue
    raise
  end

  #: Check to see if the file exists, if it does attempt to open, read, and parse
  #: it. If it is parsed the contents will be merged with the default properties
  #: overriding them.
  if File::exists?(VAGRANTFILE_JSON_PROPERTIES_OVERRIDE)
    file = open(VAGRANTFILE_JSON_PROPERTIES_OVERRIDE)
    begin
      json = file.read
      overrides = JSON.parse(json)
      props = props.deep_merge(overrides)
    rescue
      print "Vagrant encountered an error while attempting to parse: "+VAGRANTFILE_JSON_PROPERTIES_OVERRIDE
    ensure
      file.close unless file.nil?
    end
  end

  ###########################################################################
  ## VAGRANT BOX ENVIRONMENT CONFIGURATION
  ###########################################################################

  config.vm.synced_folder ".", "/vagrant"
  config.vm.network :private_network, ip: props["ip"]
  config.vm.provider :virtualbox do |vb|
    vb.gui = false
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

  #: Prepare and boot the box.
  config.vm.provision :shell, path: "provision.sh"
end
