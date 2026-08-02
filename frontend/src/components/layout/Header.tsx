import MenuIcon from "@mui/icons-material/Menu";
import NotificationsNoneOutlinedIcon from "@mui/icons-material/NotificationsNoneOutlined";
import AccountCircleOutlinedIcon from "@mui/icons-material/AccountCircleOutlined";

import AppBar from "@mui/material/AppBar";
import Avatar from "@mui/material/Avatar";
import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import Stack from "@mui/material/Stack";
import Toolbar from "@mui/material/Toolbar";
import Tooltip from "@mui/material/Tooltip";
import Typography from "@mui/material/Typography";

type HeaderProps = {
  drawerWidth: number;
  onMenuClick: () => void;
};

const Header = ({ drawerWidth, onMenuClick }: HeaderProps) => {
  return (
    <AppBar
      position="fixed"
      elevation={1}
      color="primary"
      sx={{
        width: {
          xs: "100%",
          lg: `calc(100% - ${drawerWidth}px)`,
        },
        ml: {
          xs: 0,
          lg: `${drawerWidth}px`,
        },
      }}
    >
      <Toolbar>
        {/* Mobile Menu Button */}
        <IconButton
          color="inherit"
          edge="start"
          onClick={onMenuClick}
          sx={{
            mr: 2,
            display: {
              xs: "inline-flex",
              lg: "none",
            },
          }}
        >
          <MenuIcon />
        </IconButton>

        {/* Title */}
        <Typography
          variant="h6"
          component="h1"
          sx={{
            flexGrow: 1,
            fontWeight: 600,
          }}
        >
          📚 Smart Library & Book Store
        </Typography>

        {/* Right Section */}
        <Stack
          direction="row"
          spacing={1}
          sx={{
            alignItems: "center",
          }}
        >
          <Tooltip title="Notifications">
            <IconButton color="inherit">
              <NotificationsNoneOutlinedIcon />
            </IconButton>
          </Tooltip>

          <Avatar
            sx={{
              width: 36,
              height: 36,
            }}
          >
            G
          </Avatar>

          <Box
            sx={{
              display: {
                xs: "none",
                md: "block",
              },
            }}
          >
            <Typography
              variant="body2"
              sx={{
                fontWeight: 600,
                lineHeight: 1.2,
              }}
            >
              Gaurav
            </Typography>

            <Typography
              variant="caption"
              sx={{
                opacity: 0.8,
              }}
            >
              Administrator
            </Typography>
          </Box>

          <Tooltip title="Profile">
            <IconButton color="inherit">
              <AccountCircleOutlinedIcon />
            </IconButton>
          </Tooltip>
        </Stack>
      </Toolbar>
    </AppBar>
  );
};

export default Header;