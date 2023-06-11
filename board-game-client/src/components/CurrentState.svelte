

<script>
    import RoundOrder from "./RoundOrder.svelte";

    let players = [
        {"name": "Szymon", "isCurrent": false},
        {"name": "Agata", "isCurrent": true},
        {"name": "Michał", "isCurrent": false},
    ]

    let currentRoundTime = "1:01"

</script>

    <div class="col">
      <RoundOrder {players} {currentRoundTime}/>
    </div>
