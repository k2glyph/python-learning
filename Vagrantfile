Vagrant.configure("2") do |config|
  config.vm.box = "wesmcclure/ubuntu1404-docker"
  config.vm.define "python-learning-server" do |pls|
    pls.vm.hostname = "pl-server"
    pls.vm.network "private_network", ip: "192.168.56.2"
  end
end
