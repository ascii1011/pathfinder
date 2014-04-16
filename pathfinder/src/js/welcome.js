function printSentence(id, sentence){
    var index=0; 
    var intObject= setInterval(function() {
        document.getElementById(id).innerHTML+=sentence[index]; 
        document.getElementById('audiotag1').play();
        index++;
        if(index==sentence.length){
            clearInterval(intObject);
        }
    }, 800);
}
