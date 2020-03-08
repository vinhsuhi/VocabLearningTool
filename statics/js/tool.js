// d3.select("#content")
//     .selectAll('div')
//     .data(vocab)
//     .enter()
//     .append("div")
//     .attr("class","card")
//     .html(function(d){
//         return `
//         <input type="checkbox" class="card-visitors-indicator" />
//             <div class="header">
//                 <label class="indicator" for="card-visitors-indicator">
//                     <audio class="my_audio" controls preload="none">
//                         <source src="{{ url_for('static', filename=` + d.audio + `) }}" type="audio/mpeg">
//                     </audio>
//                 </label>
//                 <div class="content">
//                     <div class="data">
//                         <div class="top">
//                             <p class="title">Visitors</p>
//                             <p class="date">01 Sep 2016 - 15 Sep 2016</p>
//                         </div>
//                         <div class="graph">
//                             <div class="horizontal">
//                             </div>
//                             <div class="vertical">
//                             </div>
//                         </div>
//                     </div>
//                     <p class="title">`+ d.eng + `</p>
//                     <div class="float"></div>
//                 </div>
//             </div>
//             <div class="info">
//                 <p class="counter">` + d.vn + `<span class="unit"></span></p>
//             </div>
//             `
//     });
// const language = {
//     ENG : true,
//     VN : false
// }

var i = 0,eng=vocab[0].eng,vn=vocab[0].vn,lang=true;

function changeLanguage(lan){
    lang = lan;
    changeWord(0);
}

function changeWord(m){
    document.getElementById('vietnam-word').value = "";
    document.getElementById('result-user').innerHTML = "";
    i += parseInt(m);
    // console.log("vinhsuhi");
    if(i >= vocab.length){
        i = vocab.length - 1;
    }
    if(i < 0){
        i = 0;
    }
    console.log(i);

    eng = vocab[i].eng;
    vn = vocab[i].vn;
    document.getElementById('eng-dict').innerHTML = lang ? eng : vn;
    // document.getElementById('vn-dict').innerHTML = vocab[i].vn;
    // document.getElementById('audio-dict').setAttribute("src",'/static' + vocab[i].audio);
    var audios = document.getElementsByTagName('audio');
    var a;
    for(a=0;a<audios.length;a++){
        audios[a].style.display = "none";
    }
    document.getElementById(vocab[i].eng).style.display = "";
}

function alertAwswer(){
    let answer = lang ? vn : eng;
    alert(answer);
    // var dialog = $(foo).dialog('open');
    // setTimeout(function() { dialog.dialog('close'); }, 3);
}


function alertFinish(){
    alert("Your Test is Finished!");
}


function checkWord(event,w){
    let answer = lang ? vn : eng;
    if(event.keyCode==13){
        document.getElementById('result-user').innerHTML = (w == answer) ? 'Good' : 'try again';
        document.getElementById('result-user').style.color = (w == answer) ? '#2FB45A' : '#DB1430';
        var audios = document.getElementsByTagName('audio');
        if(w == answer){
            audios[i].play();
            changeWord(1);
        }
        else{
            audios[i].play();
        }
        if(i == vocab.length){
            alertFinish();
        }
    }
    else{
        document.getElementById('result-user').innerHTML = "";
    }
}
