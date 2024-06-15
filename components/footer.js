import React from "react";
import styles from "../styles/Home.module.css";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <iframe
        src="https://www.facebook.com/plugins/share_button.php?href=https%3A%2F%2Fhardestmaze.com&layout&size&appId=1809798882663411&width=77&height=20"
        width="77"
        height="20"
        style={{ border: "none", overflow: "hidden" }}
        scrolling="no"
        frameborder="0"
        allowfullscreen="true"
        allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
      ></iframe>{" "}
      <a
        href="https://twitter.com/share?ref_src=twsrc%5Etfw"
        className="twitter-share-button"
        data-size="large"
        data-text="Check out this cool puzzle game!"
        data-url="https://hardestmaze.com/"
        data-related="https://twitter.com/brazealjacob"
        data-show-count="false"
      >
        Tweet
      </a>
      <span style={{ marginRight: "15px" }}>
        &copy; 2021-2024 Beren Gunsolus
      </span>{" "}
      <span style={{ color: "gray", display: "flex", fontSize: "smaller" }}>
        and{" "}
        <a target="_blank" href={"https://jacobbrazeal.com"}>
          Jacob Brazeal
        </a>
      </span>
    </footer>
  );
}
