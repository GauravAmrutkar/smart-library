import DashboardOutlinedIcon from "@mui/icons-material/DashboardOutlined";
import MenuBookOutlinedIcon from "@mui/icons-material/MenuBookOutlined";

import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

import { NavLink } from "react-router-dom";

type SidebarProps = {
  drawerWidth: number;
  mobileOpen: boolean;
  onDrawerToggle: () => void;
};

const menuItems = [
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

const Sidebar = ({
  drawerWidth,
  mobileOpen,
  onDrawerToggle,
}: SidebarProps) => {
  const drawerContent = (
    <>
      <Toolbar />

      <Box
        sx={{
          p: 2,
        }}
      >
        <Typography
          variant="h6"
          sx={{
            fontWeight: 700,
          }}
        >
          Smart Library
        </Typography>
      </Box>

      <Divider />

      <List>
        {menuItems.map((item) => (
          <ListItem
            key={item.id}
            disablePadding
          >
            <ListItemButton
              component={NavLink}
              to={item.path}
              onClick={onDrawerToggle}
              sx={{
                "&.active": {
                  bgcolor: "primary.main",
                  color: "primary.contrastText",
                },

                "&.active .MuiListItemIcon-root": {
                  color: "primary.contrastText",
                },
              }}
            >
              <ListItemIcon>
                {item.icon}
              </ListItemIcon>

              <ListItemText primary={item.title} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </>
  );

  return (
    <Box
      component="nav"
      sx={{
        width: {
          lg: drawerWidth,
        },

        flexShrink: {
          lg: 0,
        },
      }}
    >
      {/* Mobile Drawer */}

      <Drawer
        variant="temporary"
        open={mobileOpen}
        onClose={onDrawerToggle}
        ModalProps={{
          keepMounted: true,
        }}
        sx={{
          display: {
            xs: "block",
            lg: "none",
          },

          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        {drawerContent}
      </Drawer>

      {/* Desktop Drawer */}

      <Drawer
        variant="permanent"
        open
        sx={{
          display: {
            xs: "none",
            lg: "block",
          },

          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        {drawerContent}
      </Drawer>
    </Box>
  );
};

export default Sidebar;