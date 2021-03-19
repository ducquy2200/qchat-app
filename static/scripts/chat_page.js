document.addEventListener('DOMContentLoaded', () => {
  // Make 'enter' key submit messages
  let msg = document.querySelector('#user_message');
  msg.adEventListener('keyup', event => {
    event.preventDefault();
    if (event.keyCode === 13) {
      document.querySelector('#send_message').click();
    }
  })
})
