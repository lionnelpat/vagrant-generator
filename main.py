#!/usr/bin/env python


print("""
      
########################################
#                                      #
#   Welcome to Vagrant File Generator  #
#                                      #
########################################

""")

f = open("Vagrantfile", "w")

provider = input("Enter the provider: (virtualbox | vmware_desktop): ") 

vm_name = input("Enter the name of the VM: ")

box = input("Enter the box: ")

box_memory = input("Enter the memory of the box: ")

box_check_update = input("Enter the check update of the box: ")

box_gui_open = input("Enter the GUI of the box: ")

forwarded_ports = []
while (True):
    print("Enter the forwarded ports: ")
    guest =input("Enter the guest port: ")
    host = input("Enter the host port: ") 
    forwarded_ports.append({"guest": guest, "host": host})
    finish = input("Do you want to add more forwarded ports? (y/n): ")
    if (finish == "y"):
        continue
    else:
        break





# vm_name = "ubuntu"
# box = "ubuntu/bionic64"
# forwarded_ports = [
#     {"guest": 80, "host": 8080},
#     {"guest": 5432, "host": 5432},   
# ]

# synchronized_folders = [
#     {"guest": "/home/vagrant", "host": "/home/vagrant"}
# ]

# private_network = "89.0.142.86/24"

# public_network = "237.84.2.178/24"

# box_memory = 1024
# box_gui_open = False

# box_check_update = True

common_config_section = """
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  # config.vm.box = "ubuntu/trusty64"

  """

forwarded_ports_section = """
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port 


"""

private_network_section = """
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

"""

public_network_section = """
  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

"""

synchronized_folder_section = """
  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

"""

provider_section = """
  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #

"""

provision_section = """
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.

"""

commands = [
    "apt-get update",
    "\t apt-get install -y apache2"
]

shel_commands = "\n".join(commands)

if (len(forwarded_ports) > 0):
    for port in forwarded_ports:
        forwarded_ports_section += f"config.vm.network :forwarded_port, guest: {port['guest']}, host: {port['host']}\n"


# if len(private_network) > 0:
#     private_network_section += f"config.vm.network :private_network, ip: '{private_network}'\n"


# if len(public_network) > 0:
#     public_network_section += f"config.vm.network :public_network, ip: '{public_network}'\n"

# if len(synchronized_folders) > 0:
#     for folder in synchronized_folders:
#         synchronized_folder_section += f"config.vm.synced_folder '{folder['guest']}', '{folder['host']}'\n"


f.write(
f"""
Vagrant.configure("2") do |config|
    {common_config_section}
  config.vm.box = "{box}"
  config.vm.box_check_update = {box_check_update}
""" + 

forwarded_ports_section +

private_network_section +

public_network_section +

synchronized_folder_section + 

provider_section +

f""" 
  config.vm.provider :{provider} do |v|
    v.vmx["memsize"] = "{box_memory}"
    v.vmx["displayname"] = "{vm_name}"
    v.gui = {box_gui_open}
  end
"""
+

provision_section +
    
f"""
config.vm.provision "shell", inline: <<-SHELL
    {
        shel_commands
    }
    SHELL
end
"""
 
)
f.close()

print("Vagrantfile created successfully!")

