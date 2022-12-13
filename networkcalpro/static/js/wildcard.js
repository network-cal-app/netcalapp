document.addEventListener("DOMContentLoaded",()=>{

    const allBorder = document.getElementById('all');
    const all_value = document.getElementById('all_value');
    
    var all_radius = 24;
    
    const subnet = {
        1: '127.255.255.255', 2: '63.255.255.255', 3:'31.255.255.255', 4:'15.255.255.255', 5:'7.255.255.255', 6:'3.255.255.255',7: '1.255.255.255',
    8: '0.255.255.255', 9: '0.127.255.255', 10: '0.63.255.255', 11:'0.31.255.255', 12:'0.15.255.255', 13:'0.7.255.255', 14:'0.3.255.255',15:'0.1.255.255',
    16: '0.0.255.255', 17: '0.0.127.255', 18: '0.0.63.255', 19:'0.0.31.255', 20:'0.0.15.255', 21:'0.0.7.255', 22:'0.0.3.255',23:'0.0.1.255', 24: '0.0.0.255',   
    25: '0.0.0.127', 26: '0.0.0.63', 27:'0.0.0.31', 28:'0.0.0.15', 29:'0.0.0.7', 30:'0.0.0.3',
    }
    
    function allBordersUpdate(){
        all_radius = allBorder.value;
        all_value.innerText="/"+ all_radius+" or " +subnet[all_radius];
        
    }
    
    allBorder.addEventListener("mousemove",allBordersUpdate);
    allBorder.addEventListener("change",allBordersUpdate);
    
    allBordersUpdate();
    
    });
    