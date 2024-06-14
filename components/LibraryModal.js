import React from "react";
import Library from "./Library";

export default class LibraryModal extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    if (!this.props.open) return <div />;

    return (
      <div className="lib-modal__wrap">
        <div className={"lib-modal__bg"}></div>
        <div className="lib-modal">
          <div className="lib-modal__header">
            Library
            <div className="lib-modal__header__spacer" />
            <div
              className="lib-modal__header__close"
              onClick={this.props.onClose}
            >
              &#10005;
            </div>
          </div>
          <div className="lib-modal__body">
            <Library onClick={this.props.onClick} />
          </div>
        </div>
      </div>
    );
  }
}
