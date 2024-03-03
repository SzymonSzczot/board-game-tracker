<script>
    import RoundOrder from "./RoundOrder.svelte";

    let players = [
        {"name": "Szymon", "isCurrent": false, "roundTime": "01",  "points": [
                {"icon": "https://thenounproject.com/api/private/icons/256442/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=752&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
          ]},
        {"name": "Agata", "isCurrent": true, "roundTime": "11", "points": [
                {"icon": "https://thenounproject.com/api/private/icons/256442/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=752&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
                {"icon": "", "value": 30},
          ]},
        {"name": "Michał", "isCurrent": false, "roundTime": "33", points: []},
    ]

    let currentRoundTime = "1:01"

</script>

<div class="col">
  <RoundOrder {players} {currentRoundTime}/>
</div>
