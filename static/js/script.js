$(document).ready(function(){
 $("#add-cartec").click(function(){
 	var salto="<br>";
 	var cartec=$("#nombre-req-tec-input-cartec1").val();
	var cartecval=$("#nombre-req-tec-input-valor1").val();
    $(".new-desc-cartec").append(cartec,salto);
    $(".new-des-valor").append(cartecval,salto);
    });

 $("#add-cartec-comer").click(function(){
 	var salto="<br>";
 	var cartec=$("#nombre-req-tec-input-cartec2").val();
	var cartecval=$("#nombre-req-tec-input-valor2").val();
    $(".new-desc-cartec-comer").append(cartec,salto);
    $(".new-des-valor-comer").append(cartecval,salto);
    });



 $("#deslizar-coti").click(function(){
 	$("#container-cot").fadeToggle("slow");

 });
});
