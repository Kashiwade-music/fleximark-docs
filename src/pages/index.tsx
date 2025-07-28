import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import HomepageFeatures from "@site/src/components/HomepageFeatures";
import Heading from "@theme/Heading";
import Layout from "@theme/Layout";
import clsx from "clsx";
import React from "react";
import type { ReactNode } from "react";

import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header className={clsx(styles.heroSection)}>
      <div className={styles.heroContent}>
        <img
          src="img/main-product-logo.webp"
          alt="Product Logo"
          className={styles.productLogo}
        />
        <Link className={styles.ctaButton} to="/docs/intro">
          Get Started
        </Link>
        <div className={styles.screenshotWrapper}>
          <img
            src="img/vscodium.png"
            alt="Product Screenshot"
            className={styles.screenshot}
          />
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />"
    >
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
