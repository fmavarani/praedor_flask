
document.addEventListener("load", function(){
    var link = document.getElementById('exportJSON');
    link.addEventListener('click', exportJson);
    function exportJson(el) {
        console.log("Hello world!"); 
        var obj = "{&#34;name&#34;: &#34;a&#34;, &#34;role&#34;: &#34;Adventurer&#34;, &#34;archetype&#34;: &#34;Warrior&#34;, &#34;idea&#34;: &#34;a&#34;, &#34;attributes&#34;: {&#34;Strength&#34;: 5, &#34;Constitution&#34;: 10, &#34;Agility&#34;: 11, &#34;Awareness&#34;: 11, &#34;Bravery&#34;: 9, &#34;Charisma&#34;: 10}, &#34;skills&#34;: {&#34;Alchemy&#34;: 12, &#34;Bartering&#34;: 15, &#34;Blunt Weapons&#34;: 11, &#34;Bows&#34;: 15, &#34;Books &amp; Science&#34;: 11, &#34;Brawl&#34;: 10, &#34;Building&#34;: 11, &#34;Climbing &amp; Jumping&#34;: 17, &#34;Crafts&#34;: 8, &#34;Cursed Lands&#34;: 9, &#34;Dodge&#34;: 16, &#34;Gambling&#34;: 17, &#34;Healing&#34;: 16, &#34;Heraldry&#34;: 9, &#34;Herbs &amp; Poisons&#34;: 11, &#34;History&#34;: 12, &#34;Hunting&#34;: 16, &#34;Insight&#34;: 16, &#34;Intimidation&#34;: 14, &#34;Knives&#34;: 17, &#34;Languages&#34;: 7, &#34;Leadership&#34;: 14, &#34;Lock picking&#34;: 8, &#34;Lore &amp; Legends&#34;: 7, &#34;Management&#34;: 13, &#34;Occult&#34;: 8, &#34;Performing&#34;: 13, &#34;Poetry&#34;: 15, &#34;Reading&#34;: 12, &#34;Religion&#34;: 7, &#34;Riding&#34;: 12, &#34;Sailing&#34;: 9, &#34;Scheming&#34;: 17, &#34;Seduction&#34;: 14, &#34;Shields&#34;: 8, &#34;Singing &amp; Playing&#34;: 16, &#34;Sleight of Hand&#34;: 11, &#34;Sneak&#34;: 12, &#34;Spears&#34;: 13, &#34;Streetwise&#34;: 16, &#34;Survival&#34;: 13, &#34;Swimming&#34;: 9, &#34;Swords&#34;: 11, &#34;Tactics&#34;: 16, &#34;Throwing&#34;: 14, &#34;Trade Routes&#34;: 7}, &#34;wealth&#34;: -50, &#34;background&#34;: &#34;Southern Jaconia&#34;, &#34;advantages&#34;: [], &#34;disadvantages&#34;: [], &#34;equipment&#34;: [&#34;Clothes&#34;, &#34;Rucksack&#34;], &#34;experience&#34;: [], &#34;logs&#34;: []}";
        var data = "text/json;charset=utf-8," + encodeURIComponent(obj);
        // what to return in order to show download window?
    
        el.setAttribute("href", "data:"+data);
        el.setAttribute("download", "json");
     }
});
