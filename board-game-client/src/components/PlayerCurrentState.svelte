

<style>
    .isCurrent {
        box-shadow: 0 0 14px rgba(83, 91, 242, 0.5);
        font-weight: 600;
    }
</style>


<script>
    import PlayerRound from "./PlayerRound.svelte";
    import PlayerPoints from "./PlayerPoints.svelte";

    export let player;
</script>

<div class="border m-3" class:border-primary={player.isCurrent} class:isCurrent={player.isCurrent} class:border-warning={!player.isCurrent}>
  <PlayerRound {player}/>
  <hr class="my-2">
  <PlayerPoints points={player.points}/>
</div>
