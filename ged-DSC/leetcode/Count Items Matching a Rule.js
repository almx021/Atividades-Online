/*
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

// Embora não seja a solução mais eficiente,
// eu quis fazer assim para testar o uso do filter
// sem map auxiliar
var countMatches = function(items, ruleKey, ruleValue) {
    switch(ruleKey){
        case "type":
            return items.filter(item => item[0] == ruleValue).length;
        case "color":
            return items.filter(item => item[1] == ruleValue).length;
        case "name":
            return items.filter(item => item[2] == ruleValue).length;
        default:
            return 0;
        }
};

// console.log(countMatches(items, ruleKey, ruleValue))