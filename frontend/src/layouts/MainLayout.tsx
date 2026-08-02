import { useState } from "react";

import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Toolbar from "@mui/material/Toolbar";

import { Outlet } from "react-router-dom";

import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";

const DRAWER_WIDTH = 260;

const MainLayout = () => {
  const [mobileOpen, setMobileOpen] = useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen((previous) => !previous);
  };

  return (
    <Box
      sx={{
        display: "flex",
        minHeight: "100vh",
      }}
    >
      <CssBaseline />

      <Header
        drawerWidth={DRAWER_WIDTH}
        onMenuClick={handleDrawerToggle}
      />

      <Sidebar
        drawerWidth={DRAWER_WIDTH}
        mobileOpen={mobileOpen}
        onDrawerToggle={handleDrawerToggle}
      />

      <Box
        component="main"
        sx={{
          flexGrow: 1,

          bgcolor: "background.default",

          minHeight: "100vh",

          ml: {
            xs: 0,
            lg: `${DRAWER_WIDTH}px`,
          },
        }}
      >
        {/* Creates space below the fixed AppBar */}
        <Toolbar />

        <Box
          sx={{
            p: {
              xs: 2,
              sm: 3,
              md: 4,
            },
          }}
        >
          <Outlet />
        </Box>
      </Box>
    </Box>
  );
};

export default MainLayout;