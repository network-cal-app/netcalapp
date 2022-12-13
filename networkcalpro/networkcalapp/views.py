from django.shortcuts import render
import random

# Create your views here.

def result(octet):
    if len(octet) == 4 and validation(octet) == 4:
        return True
    else: 
        return False

def validation(octet):
    return validoctet(octet[0]) + validoctet(octet[1]) + validoctet(octet[2]) + validoctet(octet[3])
    
def validoctet(octets):
    if octets.isnumeric() and 0 <= int(octets) < 256:
        return 1
    else:
        return 0

def decimal_conversion(binary):
    binary_val = [128, 64, 32, 16, 8, 4, 2, 1]
    ip_address = ""
    oct_val = 0
    val = 0
    for oct in binary.split("."):
        for i in oct:
            if i == "0":
                oct_val = oct_val + 0
            else:
                oct_val = oct_val + binary_val[val]
            val = val + 1
        val = 0
        oct_val_join = str(oct_val) + "."
        ip_address = ip_address + oct_val_join
        oct_val = 0
    return ip_address[:-1]

def binary_convertion(address):
    binary_val = [128, 64, 32, 16, 8, 4, 2, 1]
    binary = ""
    for oct in address.split("."):
        for i in range(8):
            value = int(oct)%binary_val[i]
            if value == int(oct):
                binary = binary + "0"
            else:
                binary = binary + "1"
                oct = value
        binary = binary + "."
    binary = binary[:-1]
    return binary

def binary_calculation(ip):
    binary_ip_address = binary_convertion(ip[0])
    binary_subnet_mask = binary_convertion(subnet(int(ip[1])))
    index_value = 0
    binary_network_ip_address = ""
    binary_bcast_ip_address = ""
    for bit in binary_subnet_mask:
        if bit == "1":
            binary_network_ip_address = binary_network_ip_address + binary_ip_address[index_value]
            binary_bcast_ip_address = binary_bcast_ip_address + binary_ip_address[index_value]
        elif bit == ".":
            binary_network_ip_address = binary_network_ip_address + "." 
            binary_bcast_ip_address = binary_bcast_ip_address + "."
        else:
            binary_network_ip_address = binary_network_ip_address + "0" 
            binary_bcast_ip_address = binary_bcast_ip_address + "1"
        index_value = index_value + 1
    binary_first_usable_ip = binary_network_ip_address[:-1] + "1"
    binary_last_usable_ip = binary_bcast_ip_address[:-1] + "0"
    ip_address = decimal_conversion(binary_ip_address)
    subnet_mask = decimal_conversion(binary_subnet_mask)
    network_ip_address = decimal_conversion(binary_network_ip_address)
    bcast_ip_address = decimal_conversion(binary_bcast_ip_address)
    first_usable_ip = decimal_conversion(binary_first_usable_ip)
    last_usable_ip = decimal_conversion(binary_last_usable_ip)
    return {"given_ip_address":[ip_address,binary_ip_address], "subnet_mask_address":[subnet_mask,binary_subnet_mask], 
                "network_address":[network_ip_address,binary_network_ip_address], "broadcast_address":[bcast_ip_address,binary_bcast_ip_address],
                "first_usable_ip_address":[first_usable_ip,binary_first_usable_ip], "last_usable_ip_address":[last_usable_ip,binary_last_usable_ip]}

def network_calculation(ip):
    ip_address = ip.split("/")
    ip_details = binary_calculation(ip_address)
    return ip_details

def subnet(sub_n):
    mask = {
        0: '0.0.0.0', 1: '128.0.0.0', 2: '192.0.0.0', 3:'224.0.0.0', 4:'240.0.0.0', 5:'248.0.0.0', 6:'252.0.0.0',7:'254.0.0.0',
    8: '255.0.0.0', 9: '255.128.0.0', 10: '255.192.0.0', 11:'255.224.0.0', 12:'255.240.0.0', 13:'255.248.0.0', 14:'255.252.0.0',15:'255.254.0.0',
    16: '255.255.0.0', 17: '255.255.128.0', 18: '255.255.192.0', 19:'255.255.224.0', 20:'255.255.240.0', 21:'255.255.248.0', 22:'255.255.252.0',23:'255.255.254.0', 24: '255.255.255.0',   
    25: '255.255.255.128', 26: '255.255.255.192', 27:'255.255.255.224', 28:'255.255.255.240', 29:'255.255.255.248', 30:'255.255.255.252',31:'255.255.255.254', 32: '255.255.255.255',
    }
    return mask[sub_n]

    
def random_ip_network_subnet():
    ip_class = random.choice(["172.16.","192.168."])
    if ip_class == "172.16.":
        ip_second_oct = random.randint(16, 31)
        ip_address = "172." + str(ip_second_oct) + ".0.0"
        ip_subnet = random.randint(21, 30)
        detail_host_subnet = {"21":"32 subnets and 2046 hosts","22":"64 subnets and 1022 hosts","23":"128 subnets and 510 hosts", "24":"256 subnets and 254 hosts", 
                                "25":"512 subnets and 126 hosts", "26":"1024 subnets and 62 hosts", "27":"2048 subnets and 30 hosts", "28":"4096 subnets and 14 hosts", "29":"8192 subnets and 6 hosts", "30":"16384 subnets and 2 hosts"}
        ip_subnetmask = random.choice([str(ip_subnet), subnet(ip_subnet)])  
        value = ip_address + "/" + ip_subnetmask
        value_list = [value, detail_host_subnet[str(ip_subnet)]]
        return value_list

    else:
        ip_third_oct = random.randint(0, 255)
        ip_address = "192.168." + str(ip_third_oct) + ".0"
        ip_subnet = random.randint(24, 30)
        detail_host_subnet = {"24":"1 subnets and 254 hosts", "25":"2 subnets and 126 hosts", "26":"4 subnets and 62 hosts", 
                                  "27":"8 subnets and 30 hosts", "28":"16 subnets and 14 hosts", "29":"32 subnets and 6 hosts", "30":"64 subnets and 2 hosts"}
        ip_subnetmask = random.choice([str(ip_subnet), subnet(ip_subnet)])
        value = ip_address + "/" + ip_subnetmask
        value_list = [value, detail_host_subnet[str(ip_subnet)]]
        return value_list


def network_subnet():
    auestion_and_ans = random_ip_network_subnet()
    question = "How many subnets and hosts per subnet can you get from the network " + auestion_and_ans[0] + "?"
    return [question, auestion_and_ans[1]]

def ip_generat():
    ip_class = random.choice(["10.","172.16.","192.168."])
    if ip_class == "10.":
        ip_second_oct = random.randint(0, 255)
        ip_third_oct = random.randint(0, 255)
        ip_fourth_oct = random.randint(0, 255)
        ip_address = "10." + str(ip_second_oct) + "." + str(ip_third_oct) + "." + str(ip_fourth_oct)
        ip_subnet = random.randint(1, 30)
        ip = ip_address + "/" + str(ip_subnet)
        ip_subnetmask = random.choice([str(ip_subnet), subnet(ip_subnet)])

    elif ip_class == "172.16.":
        ip_second_oct = random.randint(16, 31)
        ip_third_oct = random.randint(0, 255)
        ip_fourth_oct = random.randint(0, 255)
        ip_address = "172." + str(ip_second_oct) + "." + str(ip_third_oct) + "." + str(ip_fourth_oct)
        ip_subnet = random.randint(1, 30)
        ip = ip_address + "/" + str(ip_subnet)
        ip_subnetmask = random.choice([str(ip_subnet), subnet(ip_subnet)])
    else:
        ip_third_oct = random.randint(0, 255)
        ip_fourth_oct = random.randint(0, 255)
        ip_address = "192.168." + str(ip_third_oct) + "." + str(ip_fourth_oct)
        ip_subnet = random.randint(1, 30)
        ip = ip_address + "/" + str(ip_subnet)
        ip_subnetmask = random.choice([str(ip_subnet), subnet(ip_subnet)])
    return [ip_address,ip, ip_subnetmask]

def subnet_does():
    get_ip = ip_generat()
    ip = get_ip[0]
    ip_address = get_ip[1]
    subnet = get_ip[2]
    all_ip_details = network_calculation(ip_address)
    ip_network_address = ip + "/" + subnet
    network_address_ans = all_ip_details["network_address"][0]
    question = "Which subnet does host " + ip_network_address + " belong to?"
    return [question, network_address_ans]

def valid_host_range():
    get_ip = ip_generat()
    ip = get_ip[0]
    ip_address = get_ip[1]
    subnet = get_ip[2]
    all_ip_details = network_calculation(ip_address)
    ip_network_address = ip + "/" + subnet
    first_usable_ip = all_ip_details["first_usable_ip_address"][0]
    last_usable_ip = all_ip_details["last_usable_ip_address"][0]
    valid_host_range_ans = first_usable_ip + " through to  through to " + last_usable_ip
    question = "What valid host range is the IP address " + ip_network_address + " a part of?" 
    return [question, valid_host_range_ans]

def last_valid_host():
    get_ip = ip_generat()
    ip = get_ip[0]
    ip_address = get_ip[1]
    subnet = get_ip[2]
    all_ip_details = network_calculation(ip_address)
    ip_network_address = ip + "/" + subnet
    last_usable_ip = all_ip_details["last_usable_ip_address"][0]
    question = "What is the last valid host on the subnetwork " + ip_network_address + " ?" 
    return [question, last_usable_ip]

def first_valid_host():
    get_ip = ip_generat()
    ip = get_ip[0]
    ip_address = get_ip[1]
    subnet = get_ip[2]
    all_ip_details = network_calculation(ip_address)
    ip_network_address = ip + "/" + subnet
    first_usable_ip = all_ip_details["first_usable_ip_address"][0]
    question = "What is the first valid host on the subnetwork " + ip_network_address + " ?" 
    return [question, first_usable_ip]

def gen_questions():
    return random.choice([network_subnet(), subnet_does(), valid_host_range(), 
                            last_valid_host(), first_valid_host()])

def index(request):
    ip_address = ""
    validornot = ""
    subnetwork_address = ""
    broadcast_address = ""
    first_usable_ip = ""
    last_usable_ip = ""
    text_box_ip = "Enter IP address..."
    range_value = 24
    if request.method == "POST":
        ip_address = request.POST.get("sub_ip")
        wildcard_mask = request.POST.get("all")
        octets = ip_address.split(".")
        if result(octets):
            ip = ip_address + "/" + str(wildcard_mask)
            detail_ip = network_calculation(ip)
            subnetwork_address = detail_ip["network_address"][0]
            broadcast_address = detail_ip["broadcast_address"][0]
            first_usable_ip = detail_ip["first_usable_ip_address"][0]
            last_usable_ip = detail_ip["last_usable_ip_address"][0]
            text_box_ip = ip_address
            range_value = wildcard_mask
                  
        else:
            validornot = "Please Enter a valid IP address!!!"
            ip_address = ""
            subnetwork_address = ""
            broadcast_address = ""
            first_usable_ip = ""
            last_usable_ip = ""
            text_box_ip = ip_address
            range_value = wildcard_mask
    return render(request,'networkcalapp/index.html',{"ip_address": ip_address, "validornot":validornot, "subnetwork_address": subnetwork_address, 
                    "broadcast_address":broadcast_address, "first_usable_ip":first_usable_ip, "last_usable_ip":last_usable_ip,
                    "text_box_ip":text_box_ip,"range_value":range_value})



def whildcardmask(request):
    ip_address = ""
    starting_address = ""
    validornot = ""
    ending_address = ""
    text_box_ip = "Enter IP address..."
    range_value = 24
    if request.method == "POST":
        ip_address = request.POST.get("sub_ip")
        wildcard_mask = request.POST.get("all")
        octets = ip_address.split(".")
        if result(octets):
            ip = ip_address + "/" + str(wildcard_mask)
            detail_ip = network_calculation(ip)
            starting_address = detail_ip["first_usable_ip_address"][0]
            ending_address = detail_ip["last_usable_ip_address"][0]
            text_box_ip = ip_address
            range_value = wildcard_mask
                  
        else:
            validornot = "Please Enter a valid IP address!!!"
            ip_address = ""
            starting_address = ""
            ending_address = ""
            text_box_ip = ip_address
            range_value = wildcard_mask

    return render(request,'networkcalapp/whildcardmask.html',{"ip_address": ip_address,"starting_address":starting_address,"ending_address":ending_address,"validornot":validornot,"text_box_ip":text_box_ip,"range_value":range_value})


def subnetquestions(request):
    question_and_ans = ""
    question_and_ans = gen_questions()
    subnetquestions.question_and_ans = question_and_ans
    return render(request, 'networkcalapp/subnetquestions.html',{"subnet_questions":question_and_ans[0]})


def subnetquestions_rans(request):
    question = ""
    answer = ""
    question = subnetquestions.question_and_ans[0]
    answer = subnetquestions.question_and_ans[1]
    return render(request, 'networkcalapp/subnetquestions_rans.html',{"subnet_questions":question, "subnet_answer":answer})

