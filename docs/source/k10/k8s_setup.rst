K8S Setup
=========

Kubernetes is an open-source platform for managing containers such as Docker. Is a management system that provides a platform for deployment automation. With Kubernetes, you can freely make use of the hybrid, on-premise, and public cloud infrastructure to run deployment tasks of your project.

And Docker lets you create containers for a pre-configured image and application. Kubernetes provides the next step, allowing you to balance loads between containers and run multiple containers across multiple systems.

This guidebook will walk you through How to Install Kubernetes on Ubuntu 20.04.

Environment Setup
-----------------

Using Vagrant to build the K8S Environment. This setup includes 1 master node and 2 worker nodes. 

.. list-table:: K8S Host Settings
   :widths: 25 25 50
   :header-rows: 1

   * - Hostname
     - IP Address
     - vCPU
     - vRAM
     - vDisk
     - OS
   * - k8s-master
     - 10.110.10.80
     - 4
     - 2
     - 120G
     - generic/ubuntu2004
   * - k8s-worker01
     - 10.110.10.81
     - 8
     - 4
     - 120G
     - generic/ubuntu2004
   * - k8s-worker02
     - 10.110.10.82
     - 8
     - 4
     - 120G
     - generic/ubuntu2004

Vagrant_Script:
.. code-block:: ruby

   # -*- mode: ruby -*-
    # vi: set ft=ruby :
    #
    Vagrant.require_version ">= 1.6.0"

    # All Vagrant configuration is done below. The "2" in Vagrant.configure
    # configures the configuration version (we support older styles for
    # backwards compatibility). Please don't change it unless you know what
    # you're doing.


    boxes = [
        {
            :name => "k8s-master",
            :eth1 => "10.110.10.80",
            :netmask => "255.255.255.0",
            :mem => "4096",
            :cpu => "2"

        },
        {
            :name => "k8s-worker1",
            :eth1 => "10.110.10.81",
            :mem => "8192",
            :netmask => "255.255.255.0",        
            :cpu => "4"

        },
        {
            :name => "k8s-worker2",
            :eth1 => "10.110.10.82",
            :netmask => "255.255.255.0",
            :mem => "8192",
            :cpu => "4"

        }
    ]

    Vagrant.configure(2) do |config|

    # config.vm.box = "ubuntu/jammy64"
    config.vm.box = "generic/ubuntu2004"  #ubuntu 20.04  generic/ubuntu1804  ubuntu/focal64 bento/ubuntu-20.04
    config.vm.box_download_insecure = true
    boxes.each do |opts|
        config.vm.define opts[:name] do |config|
            config.vm.hostname = opts[:name]

            config.vm.provider "vmware_fusion" do |v|
            v.vmx["memsize"] = opts[:mem]
            v.vmx["numvcpus"] = opts[:cpu]
            end

            config.vm.provider "virtualbox" do |v|
            v.customize ["modifyvm", :id, "--memory", opts[:mem]]
            v.customize ["modifyvm", :id, "--cpus", opts[:cpu]]
            end

            config.vm.provider "vmware_esxi" do |v|
            v.esxi_hostname = '10.110.10.10'
            v.esxi_username = 'root'
            v.esxi_password = 'TmL@bVeeam1'
            # v.esxi_password = 'prompt:'    
            v.esxi_virtual_network = ['vagrant-private', 'swguest110']
            v.esxi_disk_store = 'ESXI02_Datastore'
            v.guest_name = opts[:name] 
            v.guest_username = 'vagrant'
            v.guest_memsize = opts[:mem]
            v.guest_numvcpus = opts[:cpu]
            v.guest_disk_type = 'thin'
            v.guest_boot_disk_size = '30'
            v.guest_nic_type = 'e1000'
            v.guest_virtualhw_version = '14'
        
            v.debug = 'true'
        

            # v.customize ["modifyvm", :id, "--memory", opts[:mem]]
            # v.customize ["modifyvm", :id, "--cpus", opts[:cpu]]
            end

            # config.vm.network :private_network, type: "dhcp"
            config.vm.network :public_network, ip: opts[:eth1], netmask: opts[:netmask], gateway: "10.110.10.254", dns: "10.110.10.101"
        end
    end
    config.vm.provision "shell", privileged: true, path: "./setup.sh"
    end



Step-By-Step
------------

