import Head from 'next/head'
import styles from '../styles/Home.module.css'
import Controller from "./controller";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <Controller />
      </main>

      <footer className={styles.footer}>
        <a
          href="https://twitter.com/heptadecagon1"
          target="_blank"
          rel="noopener noreferrer"
        >
          By @BerenGunsolus
            {/* And @JacobBrazeal */}
        </a>
      </footer>
    </div>
  )
}
