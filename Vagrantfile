Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  # VM1 - Nó de Controle com Ansible
  config.vm.define "vm1" do |vm1|
    vm1.vm.network "private_network", ip: "192.168.56.10"
    vm1.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
    end
    vm1.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y software-properties-common
      sudo add-apt-repository --yes --update ppa:ansible/ansible
      sudo apt-get install -y ansible
    SHELL
  end

  # VM2 - Nó Gerenciado (sem provisionamento via Vagrant)
  config.vm.define "vm2" do |vm2|
    vm2.vm.network "private_network", ip: "192.168.56.11"
    vm2.vm.provider "virtualbox" do |vb|
      vb.memory = 512
    end
    vm2.vm.synced_folder ".", "/home/vagrant/vagrant_data"
  end
end