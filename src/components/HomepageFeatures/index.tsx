/* eslint-disable @typescript-eslint/no-require-imports */
import Translate, { translate } from "@docusaurus/Translate";
import Heading from "@theme/Heading";
import clsx from "clsx";
import React from "react";
import type { ReactNode } from "react";

import styles from "./styles.module.css";

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<"svg">>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: translate({ message: "Flexible Category Management" }),
    Svg: require("@site/static/img/sitemap-solid.svg").default,
    description: (
      <Translate>
        Organize notes hierarchically by category or folder. Create and edit
        them intuitively—attached images are automatically sorted in the same
        structure.
      </Translate>
    ),
  },
  {
    title: translate({ message: "Extensible Preview Features" }),
    Svg: require("@site/static/img/palette-solid.svg").default,
    description: (
      <Translate>
        Supports real-time previews in VSCode and browsers. Rich syntax
        extensions like GFM, Mermaid, ABC notation, Admonition, and tab views
        are supported. You can also add custom syntax and fully tailor the
        design.
      </Translate>
    ),
  },
  {
    title: translate({ message: "Powerful Tools for Organizing Notes" }),
    Svg: require("@site/static/img/tools-solid.svg").default,
    description: (
      <Translate>
        Features like HTML export and automatic sticky note extraction make
        daily organization easier. Creating summary notes for key information is
        simple too.
      </Translate>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
