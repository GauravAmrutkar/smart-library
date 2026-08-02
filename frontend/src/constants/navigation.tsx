import DashboardOutlinedIcon from "@mui/icons-material/DashboardOutlined";
import MenuBookOutlinedIcon from "@mui/icons-material/MenuBookOutlined";

import type { NavigationItem } from "../types/navigation";

export const navigationItems: NavigationItem[] = [
  {
    id: 1,
    title: "Dashboard",
    path: "/",
    icon: <DashboardOutlinedIcon />,
  },
  {
    id: 2,
    title: "Books",
    path: "/books",
    icon: <MenuBookOutlinedIcon />,
  },
];