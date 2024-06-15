import React from "react";
import styles from "../styles/Home.module.css";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <iframe
        src="https://www.facebook.com/plugins/share_button.php?href=https%3A%2F%2Fwww.berengunsolus.com%2F&layout=button_count&size=large&appId=1809798882663411&width=88&height=28"
        width="110"
        height="28"
        style={{ border: "none", overflow: "hidden" }}
        scrolling="no"
        frameBorder="0"
        allowFullScreen={true}
        allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
      />
      <a
        href="https://twitter.com/share?ref_src=twsrc%5Etfw"
        className="twitter-share-button"
        data-size="large"
        data-text="Check out this cool puzzle game from @heptadecagon1!"
        data-url="https://berengunsolus.com/"
        data-related="https://twitter.com/brazealjacob"
        data-show-count="false"
      >
        Tweet
      </a>
      <span style={{ marginRight: "15px" }}>&copy; 2021-2024 Beren Gunsolus</span>{" "}
      <span style={{ color: "gray", display: "flex", fontSize: "smaller" }}>
       and{" "}
        <a target="_blank" href={"https://jacobbrazeal.com"}>
          Jacob Brazeal
        </a>
      </span>
    </footer>
  );
}
