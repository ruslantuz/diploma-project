var j$ = jQuery,
    $nav = j$("#navigation"),
    $slideLine = j$("#slide-line"),
    $currentItem = j$(".current-item");

j$(function(){  
  if ($currentItem[0]) {
    $slideLine.css({
      "width": $currentItem.width(),
      "left": ($currentItem.position().left + 16)
    });
  }
  j$($nav).find("li").hover(
    function(){
      $slideLine.css({
        "width": j$(this).width(),
        "left": (j$(this).position().left + 16)
      });
    },
    function(){
      if ($currentItem[0]) {
          $slideLine.css({
            "width": $currentItem.width(),
            "left": ($currentItem.position().left + 16)
          })
      }         
    }
   );
});

