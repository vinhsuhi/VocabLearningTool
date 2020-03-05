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
var i = 0;
function changeWord(m){
    document.getElementById('vietnam-word').value = "";
    i += parseInt(m);
    document.getElementById('eng-dict').innerHTML = vocab[i].eng;
    // document.getElementById('vn-dict').innerHTML = vocab[i].vn;
    // document.getElementById('audio-dict').setAttribute("src",'/static' + vocab[i].audio);
    var audios = document.getElementsByTagName('audio');
    var a;
    for(a=0;a<audios.length;a++){
        audios[a].style.display = "none";
    }
    document.getElementById(vocab[i].eng).style.display = "";

}

function checkWord(w){
    console.log(vocab[i].vn);
    document.getElementById('result-user').innerHTML = (w == vocab[i].vn) ? 'Good' : 'Vinh Oc Cho';
    document.getElementById('result-user').style.color = (w == vocab[i].vn) ? '#2FB45A' : '#DB1430';
}