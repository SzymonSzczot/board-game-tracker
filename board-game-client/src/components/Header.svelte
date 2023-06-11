
<style>
    #playerName {
      border-color: orange;
      border-width: 5px;
      border-style: solid;
    }

    .container {
      padding: 2rem;
    }

</style>

<script>
    import Timer from './Timer.svelte'
    import RoundOrder from "./RoundOrder.svelte";
    let name = "Szymon";
    let time1 = "10:10"
    let time2 = "11:11"
    let time3 = "33:33"

    let players = [
        {"name": "Szymon", "isCurrent": false},
        {"name": "Agata", "isCurrent": true},
        {"name": "Michał", "isCurrent": false},
    ]

    let currentRoundTime = "1:01"

</script>

<div class="container text-center">
  <div class="row align-items-center">
    <div class="col align-items-center" style="display: flex; max-width: 20%">
        <div id="playerName" class="p-3">{name}</div>
    </div>
    <div class="col">
      <Timer time={time1}></Timer>
      <Timer time={time2}></Timer>
      <Timer time={time3}></Timer>
    </div>
  </div>
</div>
