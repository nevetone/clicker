
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
    var hpMultipler= 1.1;
    var baseCost=10;
    var priceMultipler = 1.1;
    var goldUpgradesAmount = 10;
    var actualPrice=baseCost*priceMultipler*goldUpgradesAmount;
    const  numberOfUpgrades = 5;

    // army'x'_name
    // army'x'_cost
    // army'x'_count
    // tam gdzie jest 'x' to jest np army1_name / zrobilem na sztywno ich 5
    // tak mysle ze mozna by generowac html za pomca funckcji .html() 
    // i tyle ile bedzie w tablicy rzeczy to mozna je z automatu wypisywac jak sie html wczyta

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
    

    class Upgrade{
        constructor(nameId,nameOfUpgrade){
            this.nameId=nameId;
            this.nameOfUpgrade=nameOfUpgrade;
            this.baseDmg=1;
            this.boughtUpgrades=0;
            this.price=0;
            this.discountMultipler=0.0;
            this.priceMultipler=0.15;
           // $(this.nameId).click(this.buyUpgrade()); 
        }
        dealDmg(){
            current -= this.baseDmg*this.boughtUpgrades/10;
        }
        buyUpgrade(){
            if(gold >= this.price){
                gold -= this.price;
                this.boughtUpgrades++;
                console.log("Kupiłeś upgrade dla "+this.nameOfUpgrade+ " za " +this.price+ " golda!" );
                this.price = this.price + (this.price*this.priceMultipler)*this.boughtUpgrades;
            }
        }
        refreshPriceAndCount(){
            $(this.nameId+'_count').text(this.boughtUpgrades);
            $(this.nameId+'_cost').text(this.price);
        }
      //  bindClick(){     
     //       $(this.nameId).click(this.buyUpgrade());
    //   }
        


    };

        $('#upgrade0').click(function(){upgradesButtonsArray[0].buyUpgrade()});
        $('#upgrade1').click(function(){upgradesButtonsArray[1].buyUpgrade()});
        $('#upgrade2').click(function(){upgradesButtonsArray[2].buyUpgrade()});
        $('#upgrade3').click(function(){upgradesButtonsArray[3].buyUpgrade()});
        $('#upgrade4').click(function(){upgradesButtonsArray[4].buyUpgrade()});

    setInterval(function(){ 
        for(var i = 0;i<numberOfUpgrades; i++){
            upgradesButtonsArray[i].dealDmg();
        }
        if (current <= 0) {
            level++;
            current = maxhp;
            hpbar =  current/maxhp*100;
            gold += 101;
            
        }
        
        if(level > maxLevel){
            if (stagePassed == stage){
            stage ++;
            stagePassed++;
            maxhp *= hpMultipler;
            current = maxhp;
            }
            level = 1;
        }
        hpbar =  current/maxhp*100;
        for(var i = 0;i<numberOfUpgrades;i++){
            upgradesButtonsArray[i].refreshPriceAndCount();
        }
        refreshHTML();
        
        }, 100);


    var upgradeNames = [   // to do klasy Upgrade
        'lucznik',
        'rycerz',
        'cwasdl',
        'asd',
        'QWE',
        
    ];
    var baseUpgradePrices = [  //  to do klasy Upgrade
        1000,
        20000,
        100000,
        500000,
        1000000,
    ];
    var upgradesButtonsArray = [];
    for(var i = 0;i<numberOfUpgrades;i++){
        upgradesButtonsArray[i]=new Upgrade( "#upgrade"+i , upgradeNames[i] );
        upgradesButtonsArray[i].price=baseUpgradePrices[i];
        //upgradesButtonsArray[i].bindClick();
    };






    $('#clickUpgrade').click(function(){
            if(gold>=actualPrice){
                gold -= actualPrice;
                clickDmg++;
                goldUpgradesAmount++;
                actualPrice=baseCost*priceMultipler*goldUpgradesAmount;
                cost10 = multiplierPrice(10, actualPrice, priceMultipler);
                cost25 = multiplierPrice(25, actualPrice, priceMultipler);
                console.log(upgradesButtonsArray[1].price);
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