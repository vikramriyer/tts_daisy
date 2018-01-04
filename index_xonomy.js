
function constructDocSpec(){
  var docSpec = {
                  "elements": {
                    "list": {
                      menu: [{
                      caption: "Append an <item>",
                      action: Xonomy.newElementChild,
                      actionParameter: "<item/>"
                      }]
                    }
                  },
                  onchange: function(){console.log("I am onchage. ");},
                  validate: function(obj){console.log("I am validate function. ");}
                };
return docSpec
}

function start(){
  var xml = "<list>This is a document rendered from db. </list>";
  var editor = document.getElementById("editor");
  var docSpec = constructDocSpec()
  Xonomy.render(xml, editor, docSpec)
  Xonomy.setMode("laic")
}
