
$(document).ready(function(){
    
    // zmienne
    var clickCount=0;
    var stage = 1;
    var stagePassed = 1;
    var clickDmg = 75;
    var level = 1;
    var maxLevel = 3;
    var gold = 0; 
    var maxhp = 100;
    var current = maxhp;
    var hpbar =  current/100*maxhp;
    var hpMultipler= 1.1;

    var baseCost=10;
    var priceMultipler = 1.1;
    var goldUpgradesAmount = 0;
    var actualPrice=baseCost*priceMultipler*goldUpgradesAmount;



    function refreshHTML(){
        $('#boughtUpgrades').text(goldUpgradesAmount);
        $('#goldPrice').text(actualPrice);
        $('#gold').text(gold);
        $('#level').text(" "+level);
        $('#maxLevel').text(maxLevel);
        $('#stage').text(stage);
        $('#max_hp').text(maxhp.toFixed(0));
        $('.current_hp').text(current);
        $('#clickDmg').text(clickDmg);
        $('.progress-bar').css('width', hpbar.toFixed(2)+'%');
        $('#clickCount').text(clickCount);

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

    $('#clickUpgrade').click(function(){
            if(gold>=actualPrice){
                gold -= actualPrice;
                clickDmg++;
                goldUpgradesAmount++;
                actualPrice=baseCost*priceMultipler*goldUpgradesAmount;
                refreshHTML();
                
            }


    });

    
    $('.click_area').click(function(){
        // funckja klikania
        clickCount++;
        current -= clickDmg;
        var hpbar =  current/100*maxhp;
        
            if (current < 0) {
                level++;
                current = maxhp.toFixed(0);
                var hpbar =  current/100*maxhp;
                gold += 101;
                console.log("Zadałes "+clickDmg +"dmg");
                
            }
            
            if(level > maxLevel){
                if (stagePassed == stage){
                stage ++;
                stagePassed++;
                maxhp *= hpMultipler;
                }
                level = 1;
            }
            refreshHTML();
    });


        
    $('.next_arrow').click(function(){
        stage++;
        level = 1;
        refreshHTML();
    });
    $('.back_arrow').click(function(){
        if(stage > 1){
            stage--;
        }
        level = 1;
        refreshHTML();
    });
    
        
});