
$(document).ready(function(){
    


    // zmienne
    var clickCount=0;
    var stage = 1;
    var stagePassed = 1;
    var clickDmg = 70;
    var level = 1;
    var maxLevel = 3;
    var gold = 0; 
    var maxhp = 100;
    var current = maxhp;
    var hpbar =  current/maxhp*100;
    var baseCost=10;
    var priceMultipler = 1.1;
    var goldUpgradesAmount = 10;
    var actualPrice = baseCost*priceMultipler*goldUpgradesAmount;

    // upgrade'unit_id'_name -> np. upgrade1_name
    // upgrade'unit_id'_cost -> np. upgrade1_cost
    // upgrade'unit_id'_count -> np. upgrade1_count
    // zrobiłem baze danych Units, / localhost:8000/admin   id- test  haslo- 123
    // automatyczne tworzenie html jest weic wystarczy wczytac to do tablicy za pomoca for django 

    //testowe tablice sa w templates/extends/base.html , bo muszą być
    


    function multiplierPrice(x, y, z){
        var currentPrice = y;
        var final = 0;
        for(var i=1; i <= x; i++){
            final += currentPrice;
            currentPrice = currentPrice*z;
        }
        return final.toFixed(0);
    }; // jakbys sprawdzal to nie jest dokladne, bo liczy np . 143.2414124 sie moza o multiplier i wychodzi jakies gowno 
    // i jak sie to mnozy to sie psuje i wychodzi wiecej niz kosztuje standardowo
    // chyba ze masz jakis inny pomysl na to, to smialo 
    var cost10 = multiplierPrice(10, actualPrice, priceMultipler);
    var cost25 = multiplierPrice(25, actualPrice, priceMultipler);
    

    function refreshHTML(){
        $('#boughtUpgrades').text(goldUpgradesAmount);
        $('#goldPrice').text(actualPrice);
        $('#gold').text(gold);
        $('#level').text(" "+level);
        $('#maxLevel').text(maxLevel);
        $('#stage').text(stage);
        $('#max_hp').text(maxhp.toFixed(0));
        $('.current_hp').text(current.toFixed(0));
        $('#clickDmg').text(clickDmg);
        $('.progress-bar').css('width', hpbar.toFixed(2)+'%');
        $('#clickCount').text(clickCount);
        $('#cost25').text(cost25);
        $('#cost10').text(cost10);

        if (stage == 1) {
            $('.back_arrow').css('overflow', 'hidden');
        }else{
            $('.back_arrow').css('overflow', 'visible');
        }
        if (stagePassed == stage) {
            $('.next_arrow').css('overflow', 'hidden');
        }else{
            $('.next_arrow').css('overflow', 'visible');
        }


    };
    refreshHTML();



    // zrobic funkcje klikania w Xy
    // $('#buy10').click(function(){
    //     if(gold>=cost10){

    //     }
    // });

    // $('#buy25').click(function(){
    //     if(gold>=cost25){
            
    //     }
    // });
    








    $('#clickUpgrade').click(function(){
            if(gold>=actualPrice){
                gold -= actualPrice;
                clickDmg++;
                goldUpgradesAmount++;
                actualPrice=baseCost*priceMultipler*goldUpgradesAmount;
                cost10 = multiplierPrice(10, actualPrice, priceMultipler);
                cost25 = multiplierPrice(25, actualPrice, priceMultipler);
            }
    });

    
    $('.click_area').click(function(){
        // funckja klikania
        clickCount++;
        current -= clickDmg;
        console.log("Zadałes "+clickDmg +"dmg");
    });


        
    $('.next_arrow').click(function(){
        stage++;
        level = 1;
    });
    $('.back_arrow').click(function(){
        if(stage > 1){
            stage--;
        }
        level = 1;
    });
    
        
});