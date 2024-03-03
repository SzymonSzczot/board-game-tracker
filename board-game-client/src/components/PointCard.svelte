
<script>
    export let value;
    export let icon;
    const defaultIcon = "https://thenounproject.com/api/private/icons/1877282/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=752&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0"

</script>

<div class="card text-center my-1">
  <div class="card-body">
    <img src="{icon ? icon : defaultIcon}" alt="Icon" class="img-fluid" style="max-height: 100px;">
    <p class="card-text">{value}</p>
  </div>
</div>
