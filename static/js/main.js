(($) => {
  $(() => {
    /* Document Ready **************/
    $('.sidenav').sidenav()
    $('.fixed-action-btn').floatingActionButton({
      hoverEnabled: true
    })
    $('.publish-modal').modal()
    $('.tap-target').tapTarget()

    let tapTargetDisplayed = store('tapTargetDisplayed')
    if (!tapTargetDisplayed) {
      M.TapTarget.getInstance($('.tap-target')).open()
      store('tapTargetDisplayed', true)
    }
  })
})(jQuery)