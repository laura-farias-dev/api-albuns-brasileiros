Vagrant.configure("2") do |config|
  # Box base para as duas VMs
  config.vm.box = "hashicorp/bionic64"

  # VM1
  config.vm.define "vm1" do |vm1|
    vm1.vm.network "private_network", ip: "192.168.56.10"
    vm1.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
    end
  end

  # VM2
  config.vm.define "vm2" do |vm2|
    vm2.vm.network "private_network", ip: "192.168.56.11"
    vm2.vm.provider "virtualbox" do |vb|
      vb.memory = 512  # Ajuste aqui se precisar mais RAM para o Flask
    end

    # Sincronização da aplicação
    vm2.vm.synced_folder ".", "/home/vagrant/vagrant_data"

    # Provisionamento da aplicação Flask
    vm2.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask flask-cors
      cd /home/vagrant/vagrant_data
      nohup python3 app.py --host=0.0.0.0 &
    SHELL
  end
end
