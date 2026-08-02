import type { ReactNode } from "react";

export interface NavigationItem {
  id: number;
  title: string;
  path: string;
  icon: ReactNode;
}