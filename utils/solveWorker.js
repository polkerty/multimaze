
// We always just respond to external messages.
// So we just need to keep track of the ID of the request we're responding to.
class Controller {
  constructor() {
    onmessage = (e) => {
      const { payload, messageId } = e.data;

      this.handle(payload, messageId);
    };

  }

  respond(payload, messageId) {
    postMessage({ payload, messageId })
  }

  handle(payload, messageId) {
    let response;
    switch( payload.action ) {
        case 'solve':
            response = this.solve(payload.definition);
            break;
        default:
            response = { error: "Action not recognized: " + payload.action}
    }
    this.respond(response, messageId);
  }

solve(definition) {
    
  }
}

controller = new Controller();
